# 🌟 CloudGann Table - Advanced GANN Dynamic Trading Calculator

A professional-grade GANN Dynamic Table application with zodiac analysis, interactive charts, and advanced trading insights.

![GANN Table Demo](https://img.shields.io/badge/Status-Active-brightgreen)
![Python](https://img.shields.io/badge/Python-3.7+-blue)
![Gradio](https://img.shields.io/badge/Gradio-Latest-orange)
![License](https://img.shields.io/badge/License-MIT-green)

## 🎯 Features

- **Advanced GANN Calculations**: Professional-grade square root calculations with customizable factors
- **Zodiac Analysis**: Complete astrological mapping with Unicode symbols
- **Angle Classification**: Cardinal, Ordinal, and Special angle detection
- **Interactive Charts**: Real-time visualization with Plotly
- **Statistical Dashboard**: Comprehensive analytics and insights
- **CSV Export**: Professional data export for further analysis
- **Modern UI**: Beautiful gradient design with responsive layout
- **Real-time Updates**: Auto-calculation as you type

## 🚀 Quick Start

### Prerequisites

```bash
Python 3.7+
pip package manager
```

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/aayeshatech/cloudgann_table.git
cd cloudgann_table
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python cloudgann_table.py
```

4. **Open your browser** and navigate to the provided local URL (typically `http://localhost:7860`)

## 📦 Dependencies

```
gradio>=4.0.0
pandas>=1.3.0
plotly>=5.0.0
```

## 🎮 Usage

### Basic Usage

1. **Set Parameters**:
   - Base Value: Starting value for calculations (e.g., 3338)
   - Factor: Increment factor (e.g., 0.11)
   - Levels: Number of up/down levels (1-50)
   - Tolerance: Angle detection tolerance in degrees

2. **View Results**:
   - **Advanced Table**: Rich HTML table with color-coded angles
   - **Data View**: Clean DataFrame for analysis
   - **Chart Analysis**: Interactive degree visualization

3. **Export Data**: Download results as timestamped CSV files

### Advanced Features

- **Angle Classification**:
  - 🟢 **Cardinal**: 90°, 180°, 270°, 360° (±tolerance)
  - 🔵 **Ordinal**: 45°, 135°, 225°, 315° (±tolerance)
  - 🟡 **Special**: 120°, 275°, 325° (±tolerance)

- **Statistical Analysis**:
  - Total levels calculated
  - Special angles detected
  - Average degree analysis
  - Value range spread

## 📊 Example Output

```
Level | Up Value | Up Degree | Up Zodiac      | Down Value | Down Degree | Down Zodiac
------|----------|-----------|----------------|------------|-------------|-------------
1     | 3,411    | 45.67°    | ♉ Taurus 15.67° | 3,266     | 123.45°     | ♋ Cancer 3.45°
2     | 3,485    | 91.23°    | ♋ Cancer 1.23°  | 3,195     | 234.56°     | ♏ Scorpio 24.56°
```

## 🎨 Screenshots

*Add screenshots of your application here*

## 🔧 Configuration

### Custom Angle Tolerances
Adjust the tolerance parameter to fine-tune special angle detection:
- Conservative: 2-3 degrees
- Standard: 5 degrees (default)
- Liberal: 10-15 degrees

### Zodiac Calculations
The application uses a 30-degree zodiac wheel:
- Aries: 0°-30°
- Taurus: 30°-60°
- Gemini: 60°-90°
- And so on...

## 🚀 Deployment

### Local Development
```bash
python cloudgann_table.py
```

### Production Deployment

**Option 1: Hugging Face Spaces**
1. Create account on [Hugging Face](https://huggingface.co/)
2. Create new Space with Gradio template
3. Upload your code
4. Add `requirements.txt`

**Option 2: Heroku**
1. Create `Procfile`: `web: python cloudgann_table.py`
2. Deploy to Heroku

**Option 3: Railway/Render**
Follow their Python deployment guides

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📈 Roadmap

- [ ] **Phase 1**: Core GANN calculations ✅
- [ ] **Phase 2**: Advanced visualizations ✅
- [ ] **Phase 3**: API integration for real-time data
- [ ] **Phase 4**: Machine learning predictions
- [ ] **Phase 5**: Mobile app development
- [ ] **Phase 6**: Multi-timeframe analysis
- [ ] **Phase 7**: Portfolio integration

## 🐛 Known Issues

- Large datasets (>100 levels) may cause performance issues
- Chart rendering may be slow on older browsers

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Aayesha Tech**
- GitHub: [@aayeshatech](https://github.com/aayeshatech)
- Project Link: [https://github.com/aayeshatech/cloudgann_table](https://github.com/aayeshatech/cloudgann_table)

## 🙏 Acknowledgments

- GANN trading methodology pioneers
- Gradio team for the amazing framework
- Plotly for interactive visualizations
- Open source community

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/aayeshatech/cloudgann_table/issues) page
2. Create a new issue with detailed description
3. Contact via GitHub discussions

---

⭐ **Star this repository if you find it useful!** ⭐
