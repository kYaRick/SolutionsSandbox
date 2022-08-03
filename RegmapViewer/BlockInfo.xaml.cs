using System.Windows.Controls;

namespace RegmapViewer
{
    /// <summary>
    /// Interaction logic for BlockInfo.xaml
    /// </summary>
    public partial class BlockInfo : UserControl
    {
        public string ComponentName { get; set; } = "";

        public BlockInfo()
        {
            InitializeComponent();
            this.DataContext = this;
        }
    }
}
