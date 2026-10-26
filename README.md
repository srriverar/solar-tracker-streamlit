# Solar Lab — Dual-Axis Solar Tracker

An English-language, animated, jury-oriented dashboard built with Streamlit. It explores the solar geometry, POA irradiance, reported energy yield, validation and preliminary bill of materials of the dual-axis PV tracking study for Bogotá, Colombia.

## Run locally

```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1

pip install -r requirements.txt
streamlit run app.py
```

The dashboard is self-contained: the frontend uses inline HTML, CSS, SVG and JavaScript. It does not call external CDNs or APIs. The browser-side controls, animation, chart exploration, jury tour and CSV download run inside Streamlit's HTML component.

## Deploy on Streamlit Community Cloud

1. Create a GitHub repository and upload this project folder.
2. Open [share.streamlit.io](https://share.streamlit.io/) and sign in with GitHub.
3. Select **Create app**, then choose the repository, branch and `app.py` as the main file.
4. Deploy. Streamlit Cloud installs `requirements.txt` automatically.

### Push the project to GitHub

From this folder, after creating an empty repository on GitHub and replacing the URL below:

```bash
git init
git add .
git commit -m "Build animated solar tracker dashboard"
git branch -M main
git remote add origin https://github.com/<YOUR-ACCOUNT>/<YOUR-REPOSITORY>.git
git push -u origin main
```

No credentials, tokens or remote repository are bundled with the app.

## Project files

- `app.py` — Streamlit entry point; injects source data into the embedded frontend.
- `dashboard.html` — responsive English dashboard template, animations, SVG visualizations and client-side interactions.
- `preview.html` — standalone, fully populated HTML preview (not required by Streamlit).
- `data.py` — source values transcribed from the supplied article and thesis PDFs.
- `requirements.txt` — minimal runtime dependency.
- `.streamlit/config.toml` — wide-page theme.

## Interactions and animation

- Animated Sun path and two-axis panel orientation; play/pause day sweep.
- Date, local time, location and coordinate controls; live solar elevation, azimuth, declination, zenith, POA components and idealized STC power.
- Animated annual article comparison; pointer/touch exploration of the thesis's 365-day series; selectable monthly PVGIS inputs.
- Currency switch for the prototype bill of materials; component breakdown; CSV export.
- Guided jury tour, animated counters, chart reveals, moving clouds, orbiting rings, solar glows, chart strokes and responsive layouts.
- `prefers-reduced-motion` support.

## Source-data transparency

The headline values follow `ArticuloCesar.pdf`; the day-by-day series is transcribed from thesis Table 7 and kept separate. The interface flags differences between the two documents in daily generation, annual totals, SPA errors and the PVGIS deviation. The live irradiance display is an exploratory geometric estimate using monthly Bogotá resource inputs, not an hourly weather forecast or a replacement for the Simulink results.
