import os
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def generate_text_animation(title, lines, size="youtube", output_dir="videos"):
    os.makedirs(output_dir, exist_ok=True)

    # Set resolution and aspect ratio
    if size == "shorts":
        width, height = 7.2, 12.8
    elif size == "reels":
        width, height = 10.8, 19.2
    else:  # default youtube
        width, height = 12.8, 7.2

    fig, ax = plt.subplots(figsize=(width, height))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 1)
    ax.axis('off')
    text = ax.text(5, 0.5, "", fontsize=48, color='blue', ha='center', va='center')

    def update(frame):
        if frame < len(lines):
            text.set_text(lines[frame])
        else:
            text.set_text("")
        return text,

    anim = FuncAnimation(fig, update, frames=len(lines)+2, interval=1500, blit=True)

    filename = f"{output_dir}/{title.strip().replace(' ', '_')}.mp4"
    anim.save(filename, fps=1, extra_args=['-vcodec', 'libx264'])
    return filename
