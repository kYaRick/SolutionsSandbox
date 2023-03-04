using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading.Tasks;
using System.Windows;

namespace TestPlanCreator
{
    internal class ApplicationViewModel : INotifyPropertyChanged
    {
        public event PropertyChangedEventHandler? PropertyChanged;

        public void OnPropertyChanged([CallerMemberName] string prop = "")
        {
            if (PropertyChanged != null)
                PropertyChanged(this, new PropertyChangedEventArgs(prop));
        }

        public ObservableCollection<UIElement> Graphic
        {
            get { return graphProcessor.Graphic; }
        }
        public ObservableCollection<UIElement> this[int id]
        {
            get { return graphProcessor.GetSignalGraph(1); }
        }

        private GraphProcessor graphProcessor;
        public ApplicationViewModel()
        {
            graphProcessor = new GraphProcessor();
        }
    }
}
