# power-stat-visualizer
Power Trace Statistic Visualizer  
D3.js + Flask Interactive Histogram Viewer

## Setup
```bash
# backend (port 5000 by default)
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
flask run

# frontend (port 3000 by default)
cd frontend
npm install
npx serve .
```