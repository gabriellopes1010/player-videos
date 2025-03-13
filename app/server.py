import re
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory="/mnt/SSD/player_video_project/Full_Cycle_3.0"),
    name="static",
)
app.mount("/app", StaticFiles(directory="./assets/"), name="app")


@app.get("/", response_class=HTMLResponse)
async def server_html():
    html_file_path = Path(__file__).parent / "index.html"
    with open(html_file_path, "r", encoding="utf-8") as f:
        return f.read()


def natural_sort_key(text):
    """Ordenação natural para considerar números corretamente"""
    return [
        int(part) if part.isdigit() else part.lower()
        for part in re.split(r"(\d+)", text)
    ]


@app.get("/videos")
async def list_videos():
    BASE_DIR = Path("/mnt/SSD/player_video_project/Full_Cycle_3.0")
    video_data = {}

    if not BASE_DIR.exists():
        return {"error": "Diretório não encontrado"}

    # Captura todos os módulos e os ordena numericamente e alfabeticamente
    modules = sorted(
        [module for module in BASE_DIR.iterdir() if module.is_dir()],
        key=lambda x: natural_sort_key(x.name),
    )

    for module in modules:
        video_data[module.name] = {}

        # Captura todas as seções dentro do módulo e ordena alfabeticamente
        sections = sorted(
            [section for section in module.iterdir() if section.is_dir()],
            key=lambda x: natural_sort_key(x.name),
        )

        for section in sections:
            video_data[module.name][section.name] = sorted(
                [
                    file.name
                    for file in section.iterdir()
                    if file.suffix in [".mp4", ".zip", ".txt"]
                ],
            )

    return video_data


@app.get("/download/{module}/{section}/{filename}")
async def download_file(module: str, section: str, filename: str):
    file_path = Path(
        f"/mnt/SSD/player_video_project/Full_Cycle_3.0/{module}/{section}/{filename}"
    )

    if file_path.exists() and file_path.is_file():
        return FileResponse(
            file_path, media_type="application/octet-stream", filename=filename
        )
    else:
        raise HTTPException(status_code=404, detail="File not found")
