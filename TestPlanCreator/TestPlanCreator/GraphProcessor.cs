using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Media;
using System.Windows.Shapes;

namespace TestPlanCreator
{
    internal class GraphProcessor : INotifyPropertyChanged
    {
        public event PropertyChangedEventHandler? PropertyChanged;
        public void OnPropertyChanged([CallerMemberName] string prop = "")
        {
            if (PropertyChanged != null)
                PropertyChanged(this, new PropertyChangedEventArgs(prop));
        }

        public ObservableCollection<UIElement> Graphic;
        public ObservableCollection<SignalView> SignalsViews;

        public ObservableCollection<UIElement> GetSignalGraph(int tp)
        {
            return SignalsViews[tp].Graphic;
        }
        public GraphProcessor()
        {
            GPOpener myGPOpener = new GPOpener(@"_design.gp6");

            SignalGraph signalGraph = new SignalGraph(myGPOpener.Signals[13]);

            signalGraph.Height = 120;
            signalGraph.Width = 1000;

            Graphic = new ObservableCollection<UIElement>();
         
            Graphic.Add(signalGraph);

            OnPropertyChanged("Graphic");
        }
    }
}
