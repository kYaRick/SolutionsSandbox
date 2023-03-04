using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;

namespace TestPlanCreator
{
    internal class SignalView
    {
        public ObservableCollection<UIElement> Graphic;

        public Signal signal;

        public bool Visible;

        public int number;
    }
}
