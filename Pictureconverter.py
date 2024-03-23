from PIL import Image
import os

# from https://pythonhint.com/post/6698662917296068/pil-convert-gif-frames-to-jpg
# and https://pythonexamples.org/python-check-if-path-is-file-or-directory/

dataPath = 'Genres'

try:
    for subdir in os.listdir(dataPath):
        current_path = os.path.join(dataPath, subdir)
        for file in os.listdir(current_path):
            if os.path.isfile(os.path.join(current_path, file)): # exclude folders
                if file[-3:] == "gif":
                    with Image.open(os.path.join(current_path, file)) as im:
                        if im.format == "GIF":
                            for frame_num in range(im.n_frames):
                                # select the current frame
                                im.seek(frame_num)

                                # create a new JPEG image with the same size and mode as the GIF frame
                                jpeg_frame = Image.new('RGB', im.size)

                                # paste the current frame onto the jpeg image
                                jpeg_frame.paste(im)

                                # save the jpeg image with a filename that includes the current frame number
                                jpeg_filename = str(file).replace(".gif",".jpg")
                                jpeg_frame.save(os.path.join(current_path, jpeg_filename))
                                break
                        else: # format is already jpg
                            jpeg_filename = str(file).replace(".gif",".jpg")
                            jpeg_frame.save(os.path.join(current_path, jpeg_filename))
except Exception as e:
    print(e)
