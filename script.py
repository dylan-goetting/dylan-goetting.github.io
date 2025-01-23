from PIL import Image

# Load your existing GIF
input_gif_path = "images/clip.gif"  # Path to your existing GIF
output_gif_path = "images/clip_loop_forever.gif"  # Path for the modified GIF

# Open the GIF
with Image.open(input_gif_path) as gif:
    # Save the GIF with loop set to 0 (infinite looping)
    gif.save(output_gif_path, save_all=True, loop=0)

print(f"GIF has been modified to loop forever and saved as {output_gif_path}")
