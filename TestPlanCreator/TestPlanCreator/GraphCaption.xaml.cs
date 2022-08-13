using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace TestPlanCreator
{
    /// <summary>
    /// Interaction logic for GraphLine.xaml
    /// </summary>
    public partial class GraphCaption : UserControl, INotifyPropertyChanged
    {
        private int pinNumber;
        public string PIN_Name
        {
            get { return "PIN" + pinNumber; }
        }

        private string signalName;
        public string Signal_Name
        {
            get { return signalName; }
        }

        private int TPNumber;
        public string TP_Name
        {
            get { return "TP" + TPNumber; }
        }

        private string genName;
        public string Gen_Name
        {
            get { return genName; }
        }

        public event PropertyChangedEventHandler? PropertyChanged;

        public void OnPropertyChanged([CallerMemberName] string prop = "")
        {
            if (PropertyChanged != null)
                PropertyChanged(this, new PropertyChangedEventArgs(prop));
        }
        public GraphCaption()
        {
            InitializeComponent();

            DataContext = this;

            pinNumber = 12;
            signalName = "DFF_nQ";
            TPNumber = 10;
            genName = "Inp1";
        }
    }
}
