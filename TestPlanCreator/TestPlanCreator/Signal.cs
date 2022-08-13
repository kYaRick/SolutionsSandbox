using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;

namespace TestPlanCreator
{
    public class Signal
    {
        private int testPoint;

        public int TP
        {
            get { return testPoint; }
            set { testPoint = value; }
        }

        private int pin;

        public int PIN
        {
            get { return pin; }
            set { pin = value; }
        }

        private string name = string.Empty;
        public string Name
        {
            get { return name; }
            set { name = value; }
        }

        private int repeatCount;

        public int RepeatCount
        {
            get { return repeatCount; }
            set { repeatCount = value; }
        }

        private ObservableCollection<Point> data = new ObservableCollection<Point>();

        public ObservableCollection<Point> Data
        {
            get { return data; }
            set { data = value; }
        }


    }
}
