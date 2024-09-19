# Dota2 Autoaccepter

Accepts your DotA2 games when refresh yourself between games.

Tested on:
- Ubuntu 20.04 LTS
- Resolution: 1920x1080px

## How to use
1. Install Dota2-Autoaccepter
2. In DotA enable "Bring Dota 2 to front when match found" setting (Options > Advanced Options)
3. Start the Autoaccepter

## Features
- [X] Automatically accept a game when one is found.
- [ ] Requeue if the queue misses.
- [ ] Click "READY" during party ready check.
- [ ] Cross-platform: Works on Windows too
- [ ] Automatically tab into Dota 2 and click "Accept" or "READY" when a game is found.

## How it works?
The script takes a screenshot every 3 seconds.
It looks for the pattern of the accept button.
If the threshold requirements are exceeded, the script presses `ENTER`.

The templates (pictures of the edges of the accept button) are located in `templates/` directory.

## Installation

### Prerequisites

- Python 3.x
- Pip (Python package installer)

### Development
    ```bash
    git clone https://github.com/zwoefler/Dota2-Autoaccepter.git
    cd Dota2-Autoaccepter

    # Create Virtual Environment
    python3 -m venv Env
    source Env/bin/activate

    # Install Requirements
    pip install -r requirements.txt

    # Run Autoaccepter
    python -m autoaccepter
    ```

### Test - Run all functional tests
```BASH
python3 -m unittest discover -s tests
```

## License

MIT License - see the [LICENSE](LICENSE) file for details.

