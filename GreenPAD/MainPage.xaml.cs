namespace GreenPAD
{
    public partial class MainPage : ContentPage
    {
        private DisplayOrientation orientation;

        public MainPage()
        {
            InitializeComponent();
            Loaded +=MainPage_Loaded;
            //DeviceDisplay.Current.MainDisplayInfoChanged += Current_MainDisplayInfoChanged;
        }

        private void MainPage_Loaded(object sender, EventArgs e)
        {
            orientation = DeviceDisplay.Current.MainDisplayInfo.Orientation;
        }

        private void OnCounterClicked(object sender, EventArgs e)
        {

        }

        private void Current_MainDisplayInfoChanged(object sender, DisplayInfoChangedEventArgs e)
        {
            if (orientation != DeviceDisplay.Current.MainDisplayInfo.Orientation)
                orientation = DeviceDisplay.Current.MainDisplayInfo.Orientation;
        }
    }
}