using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
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
using TestPlanCreator.ViewModels;

namespace TestPlanCreator
{
    /// <summary>
    /// Interaction logic for SignalGraph.xaml
    /// </summary>
    public partial class SignalGraph : UserControl
    {

        private Signal signal;

        public static readonly DependencyProperty GraphicProperty =
      DependencyProperty.Register("Items1", typeof(ObservableCollection<UIElement>), typeof(SignalGraph), new PropertyMetadata(null));

        public ObservableCollection<UIElement> Graphic
        {
            get { return (ObservableCollection<UIElement>)GetValue(GraphicProperty); }
            set { SetValue(GraphicProperty, value); }
        }

        private int stepX = 40;
        private int stepY = 30;
        private void AddGrid()
        {
            SolidColorBrush gridBrush = new SolidColorBrush();
            gridBrush.Color = Colors.WhiteSmoke;

            // Set Line's width and color  


            for (int x = 0; x < ActualWidth; x += stepX)
            {
                Line tempLine = new Line();

                tempLine.X1 = x;
                tempLine.Y1 = 0;
                tempLine.X2 = x;
                tempLine.Y2 = ActualHeight;

                tempLine.StrokeThickness = 1;
                tempLine.StrokeDashArray = new DoubleCollection() { 2 };
                tempLine.Stroke = gridBrush;

                Graphic.Add(tempLine);
            }

            for (int y = 0; y < ActualWidth; y += stepY)
            {
                Line tempLine = new Line();

                tempLine.X1 = 0;
                tempLine.Y1 = y;
                tempLine.X2 = ActualWidth;
                tempLine.Y2 = y;

                tempLine.StrokeThickness = 1;
                tempLine.StrokeDashArray = new DoubleCollection() { 2 };
                tempLine.Stroke = gridBrush;

                Graphic.Add(tempLine);
            }
        }

        private void BuildSignal()
        {
            double kX = ActualWidth / signal.Data.Last().X;

            double yMax = signal.Data.MaxBy(p => p.Y).Y;
            double yMin = signal.Data.MinBy(p => p.Y).Y;

            double kY = ActualHeight / (yMax);

            Polyline polyline = new Polyline();
            SolidColorBrush signalBrush = new SolidColorBrush();
            signalBrush.Color = Colors.DarkRed;

            signal.Data.ToList().ForEach(p =>
            {
                polyline.Points.Add(new Point(kX * p.X, ActualHeight - kY * p.Y));
            });

            
            polyline.Stroke = signalBrush;
            polyline.StrokeThickness = 2;

            Graphic.Add(polyline);
        }
        public SignalGraph(Signal signal)
        {
            InitializeComponent();

            DataContext = this;

            this.signal = signal;

            Graphic = new ObservableCollection<UIElement>();



            OnPropertyChanged("Graphic");

        }

        private void UserControl_Loaded(object sender, RoutedEventArgs e)
        {
            AddGrid();

            BuildSignal();
        }
    }
}
