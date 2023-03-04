using System.ComponentModel;
using System.Runtime.CompilerServices;

namespace TestPlanCreator.ViewModels
{
    internal abstract class ViewModelsBase : INotifyPropertyChanged
    {
        public event PropertyChangedEventHandler? PropertyChanged;
        public void OnPropertyChanged([CallerMemberName] string prop = "")
        {
            if (PropertyChanged != null)
                PropertyChanged(this, new PropertyChangedEventArgs(prop));
        }
    }
}
