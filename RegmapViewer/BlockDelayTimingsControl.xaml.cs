using System.Windows.Controls;

namespace RegmapViewer
{
    /// <summary>
    /// Interaction logic for BlockDelayTimingsControl.xaml
    /// </summary>
    public partial class BlockDelayTimingsControl : UserControl
    {
        public double FullRangeMin {get; set; }
        public double FullRangeTyp { get; set; }
        public double FullRangeMax { get; set; }
        public double FullRangeUnit { get; set; }

        public double Tw5RangeMin { get; set; }
        public double Tw5RangeTyp { get; set; }
        public double Tw5RangeMax { get; set; }
        public double Tw5RangeUnit { get; set; }

        public BlockDelayTimingsControl()
        {
            InitializeComponent();
            this.DataContext = this;
        }
    }
}
