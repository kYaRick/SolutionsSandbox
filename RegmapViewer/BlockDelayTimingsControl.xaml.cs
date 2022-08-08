using System.ComponentModel;
using System.Windows;
using System.Windows.Controls;

namespace RegmapViewer
{
    /// <summary>
    /// Interaction logic for BlockDelayTimingsControl.xaml
    /// </summary>
    public partial class BlockDelayTimingsControl : UserControl
    {


        public double FullRangeMin
        {
            get { return (double)GetValue(FullRangeMinProperty); }
            set { SetValue(FullRangeMinProperty, value); }
        }

        // Using a DependencyProperty as the backing store for FullRangeMin.  This enables animation, styling, binding, etc...
        public static readonly DependencyProperty FullRangeMinProperty =
            DependencyProperty.Register("FullRangeMin", typeof(double), typeof(BlockDelayTimingsControl), new PropertyMetadata(0.0));


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
