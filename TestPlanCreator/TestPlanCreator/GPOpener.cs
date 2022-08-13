using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Xml.Linq;

namespace TestPlanCreator
{
    internal class GPOpener
    {
        public List<Signal> Signals { get; set; }

        private List<XElement> platforms;

        private double minVDD;

        public double MinVDD
        {
            get { return minVDD; }
            set { minVDD = value; }
        }

        private double maxVDD;
        public double MaxVDD
        {
            get { return maxVDD; }
            set { maxVDD = value; }
        }

        private double typVDD;
        public double TypVDD
        {
            get { return typVDD; }
            set { typVDD = value; }
        }

        private int simulationEND;

        public int SimulationEND
        {
            get { return simulationEND; }
            set { simulationEND = value; }
        }

        public GPOpener(string name)
        {
            XDocument xml;

            try
            {
                xml = XDocument.Load(name);
            }
            catch (Exception ex)
            {
                throw new Exception(ex.ToString());
            }

            try
            {
                var GPDProjectElement = xml.Element("GPDProject");

                platforms = GPDProjectElement.Element("emulatorConfiguration").Elements("platform").ToList();

                Signals = GetSignalsfromTPList(GetTPList(1));

                var vddSpecsElement = GPDProjectElement.Element("projectData").Element("specs").Element("vddSpecs");

                minVDD = Double.Parse(vddSpecsElement.Attribute("vddMin").Value.Replace('.', ','));
                typVDD = Double.Parse(vddSpecsElement.Attribute("vddTyp").Value.Replace('.', ','));
                maxVDD = Double.Parse(vddSpecsElement.Attribute("vddMax").Value.Replace('.', ','));

                var simulationPresetElement = GPDProjectElement.Element("simulationConfiguration").Element("draftPreset").Element("simulationPreset");

                var simulationENDs = simulationPresetElement.Element("transientAnalyses").Element("transientAnalysis").Attribute("stopTime").Value;

                int k;
                if (simulationENDs[simulationENDs.Length - 1] == 'm')
                {
                    simulationENDs = simulationENDs.Remove(simulationENDs.Length - 1);
                    k = 1;
                }
                else
                {
                    k = 1000;
                }

                simulationEND = k * Int16.Parse(simulationENDs);

                simulationPresetElement.Element("components").Elements("component").ToList().ForEach(c =>
                {
                    if (c.Element("componentId").Attribute("componentType").Value == "43")
                    {
                        c.Element("schematicProps").Elements("param").ToList().ForEach(p =>
                        {
                            if (p.Attribute("id").Value == "custom_signal_values")
                            {
                                var points = ParseSimulationCustomSignalGenerator(p.Attribute("value").Value);
                                Signals.Add(new Signal() { Data = points });
                            }
                            if (p.Attribute("id").Value == "lp_values")
                            {
                                var points = ParseSimulationLogicGenerator(p.Attribute("value").Value);
                                Signals.Add(new Signal() { Data = points });
                            }
                        });
                    }

                });

            }
            catch (Exception ex)
            {
                throw new Exception(ex.ToString());
            }

        }
        //GenType="8" - I2C
        //GenType="7" - Logic pattern
        //GenType="5" - const voltage
        //GenType="6" - sin
        //GenType="1" - custom signal
        //GenType="2" - logic generator
        //GenType="4" - trapezee
        private List<XElement> GetTPList(int id)
        {
            XElement platform = platforms.First(el => (string)el.Attribute("id") == id.ToString());

            return platform.Element("lastConfiguration").Element("SaveEmulator").Element("TestPoints").Elements("TPC").ToList();
        }
        private ObservableCollection<Point> ParseEmulationCustomSignalGenerator(string generatorData)
        {
            ObservableCollection<Point> points = new ObservableCollection<Point>();

            generatorData.Split(';').ToList().ForEach(br =>
            {
                int comaIndex = br.IndexOf(',') + 1;

                string t_s = br.Substring(br.IndexOf('(') + 1, comaIndex - 2).Replace(',', ' ').Replace('(', ' ').Replace(')', ' ');
                string A_s = br.Substring(comaIndex, br.Length - comaIndex - 1).Replace(',', ' ').Replace('(', ' ').Replace(')', ' ');

                int t = Int16.Parse(t_s);
                int A = Int16.Parse(A_s);

                points.Add(new Point(t, A));
            });

            return points;
        }

        private ObservableCollection<Point> ParseSimulationGenerator(string generatorData, bool logic)
        {
            ObservableCollection<Point> points = new ObservableCollection<Point>();

            generatorData.Split('|').ToList().ForEach(br =>
            {
                int spaceIndex = br.IndexOf(' ') + 1;

                double k = 1000;

                string t_s = br.Substring(0, spaceIndex).Replace('.', ',');

                switch (t_s[t_s.Length - 2])
                {
                    case 'm':
                        k = 1;
                        break;
                    case 'u':
                        k = 1.0 / 1000;
                        break;
                    default:
                        break;
                }
                t_s = t_s.Replace('m', ' ').Replace('u', ' ');

                string A_s = br.Substring(spaceIndex, br.Length - spaceIndex).Replace('.', ',');

                var t = Double.Parse(t_s);
                var A = Double.Parse(A_s);

                if (logic)
                {
                    if (points.Count < 1)
                    {
                        points.Add(new Point(0, A));
                    }
                    else
                    {
                        points.Add(new Point(points.Last().X, A));
                    }

                    points.Add(new Point(points.Last().X + t * k, A));
                }
                else
                {
                    points.Add(new Point(t * k, A));
                }
            });

            return points;
        }
        private ObservableCollection<Point> ParseSimulationLogicGenerator(string generatorData)
        {
            return ParseSimulationGenerator(generatorData, true);
        }
        private ObservableCollection<Point> ParseSimulationCustomSignalGenerator(string generatorData)
        {
            return ParseSimulationGenerator(generatorData, false);
        }
        private List<Signal> GetSignalsfromTPList(List<XElement> TPs)
        {
            List<Signal> signals = new List<Signal>();

            TPs.ForEach(tp =>
            {
                int tp_id = Int16.Parse(tp.Attribute("ID").Value);

                signals.Add(new Signal() { TP = tp_id });

                if (tp.Attribute("Type").Value == "8")
                {
                    var g = tp.Element("GeneratorOpt").Attribute("GenType");

                    switch (tp.Element("GeneratorOpt").Attribute("GenType").Value.ToString())
                    {
                        case "1":
                            signals.Last().Data = ParseEmulationCustomSignalGenerator(tp.Element("GeneratorOpt").Element("userDefinedGenerator").Element("data").Value.ToString());
                            break;
                        default:
                            break;
                    }

                }


            });

            return signals;
        }
    }
}
