# Happy Birthday Cake - Interactive Python Animation

[![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Turtle Graphics](https://img.shields.io/badge/Graphics-Turtle-green.svg)](https://docs.python.org/3/library/turtle.html)

A beautiful, interactive birthday cake animation created with Python's Turtle Graphics! This project displays a stunning multi-layered pink and purple themed birthday cake with candles, hearts, stars, and a personalized birthday message.

![Birthday Cake Animation](https://img.shields.io/badge/Status-Active-success)

## Demo Video

https://github.com/user-attachments/assets/your-video-id-here.mp4

> **Note:** To update the video above, edit this README file on GitHub.com, delete the placeholder link above, and drag & drop your `Happy.mp4` file directly into the editor. GitHub will automatically upload it and generate the correct URL.

**Alternative:** [Download the demo video](assets/Happy.mp4) to view locally.

> **Note:** The birthday cake animation showcases the beautiful pink and purple themed cake with candles, hearts, and stars! 

## Features

- **Beautiful Pink & Purple Color Palette** - Soft pink, lavender, rose, and gold tones
- **Realistic Multi-Layered Cake** - Three gorgeous layered tiers with decorative frosting
- **Animated Candles** - Five colorful candles with golden flames
- **Decorative Hearts** - Strategically placed hearts around the scene
- **Sparkling Stars** - Gold and pink stars for extra magic
- **Personalized Message** - Customizable birthday greeting
- **Dark Background** - Elegant dark theme to make colors pop

## Demo

When you run the program, you'll see:
1. A beautiful dark lavender background
2. A three-tiered cake being drawn layer by layer
3. Five colorful candles with glowing flames
4. Hearts and stars decorating the scene
5. A personalized "Happy Birthday!" message

## Quick Start

### Prerequisites

- Python 3.6 or higher
- The `turtle` module (comes pre-installed with Python)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/1AyaNabil1/Happy_Birth_Day_Cake.git
cd Happy_Birth_Day_Cake
```

2. Run the program:
```bash
python src/birthday_cake.py
```

## Customization

You can easily customize the animation by modifying the following:

### Change the Birthday Person's Name
Edit `src/birthday_cake.py`:
```python
turtle.write("Queen Ayoya 👑", align="center", font=("Brush Script MT", 30, "bold"))
# Change "Queen Ayoya" to any name you like!
```

### Change Color Theme
```python
# Background color
bg.bgcolor("#2C0E18")  # Change to any hex color

# Modify cake layer colors
turtle.fillcolor("#E6B0E6")  # Light purple, pink, etc.
```

### Adjust Candle Count
```python
candle_positions = [-60, -30, 0, 30, 60]  # Add or remove positions
```

For more customization examples, check out the [`examples/`](examples/) folder!

## Project Structure

```
Happy_Birth_Day_Cake/
│
├── src/                     # Source code
│   ├── birthday_cake.py     # Main animation script
│   └── README.md            # Source code documentation
│
├── assets/                  # Media assets
│   ├── Happy.mp4            # Demo video
│   └── README.md            # Assets documentation
│
├── docs/                    # Documentation
│   ├── CONTRIBUTING.md      # Contribution guidelines
│   ├── CHANGELOG.md         # Version history
│   ├── REQUIREMENTS.md      # System requirements
│   ├── SETUP_GUIDE.md       # Setup and Git guide
│   └── README.md            # Documentation index
│
├── examples/                # Example variations (coming soon)
│   └── README.md            # Examples documentation
│
├── README.md                # Project overview (you are here!)
├── LICENSE                  # MIT License
├── .gitignore               # Git ignore file
└── upload_to_github.sh      # Automated upload script
```

## Technical Details

- **Language**: Python 3
- **Graphics Library**: Turtle Graphics
- **Drawing Speed**: Optimized for smooth animation
- **Window Size**: 800x700 pixels
- **Compatibility**: Cross-platform (Windows, macOS, Linux)

## How It Works

1. **Setup**: Creates a turtle graphics window with custom dimensions and background
2. **Cake Layers**: Draws three rectangular layers with different pink/purple shades
3. **Frosting**: Adds decorative frosting borders using thick pen strokes
4. **Decorations**: Places colorful dots on each cake layer
5. **Candles**: Draws rectangular candles with teardrop-shaped flames
6. **Hearts & Stars**: Adds decorative elements around the cake
7. **Text**: Displays the birthday message in beautiful fonts

## Contributing

Contributions are welcome! Please read our [Contributing Guidelines](docs/CONTRIBUTING.md) for details on:
- How to report bugs
- How to suggest enhancements
- Pull request process
- Code style guidelines

## Documentation

- **[Setup Guide](docs/SETUP_GUIDE.md)** - Git setup and upload instructions
- **[Requirements](docs/REQUIREMENTS.md)** - System requirements and dependencies
- **[Changelog](docs/CHANGELOG.md)** - Version history and updates
- **[Contributing](docs/CONTRIBUTING.md)** - How to contribute to this project

---

<div align="center">
  <em>Built by AyaNexus 🦢</em>
</div>
