using System.Windows;
using System.Windows.Controls;
using System.Linq;

namespace ExplorerTemp
{
    /// <summary>
    /// Interaction logic for LauncherWindow.xaml
    /// </summary>
    public partial class LauncherWindow : Window
    {
        public LauncherWindow()
        {
            InitializeComponent();
        }

        private void Window_Loaded(object sender, RoutedEventArgs e)
        {
            var tw = new TreeViewItem { Header = "0", Items = { "0.0", "0.1" } };

            FolderView.Items.Add(tw);
            FolderView.Items.Add(new TreeViewItem { Header = "1" });
            FolderView.Items.Add(new TreeViewItem { Header = "2" });
        }
    }
}
