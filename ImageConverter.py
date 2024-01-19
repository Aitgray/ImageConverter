# This program is intended to convert heic files into JPG files

import os
import subprocess
import sys
import torch
from PIL import Image
import face_recognition

def load_images(directory):
    images = []
    for filename in os.listdir(directory):
        if filename.endswith('.heic'):
            images.append(filename)
    return images

# This function will convert the heic files into jpg files
def convert_heic_to_jpg(images):
    # Iterate through the list of images
    for image in images:
        # Use the subprocess library to convert the heic files into jpg files
        subprocess.run(['heif-convert', image, image[:-5] + '.jpg'])
        # Delete the heic files
        os.remove(image)
    return 0
    

# This function will sort the photos into folders based on the content in the photos
# To achieve this we will use the pytorch library. I will ignore all of the photos
# with people in them for now and sort them later, but I want all the photos with
# animals, landscapes, and objects to be sorted into folders
def sort(images):
    # Load the model
    model = torch.hub.load('pytorch/vision:v0.6.0', 'resnet18', pretrained=True)
    # Set the model to evaluation mode
    model.eval()
    # Create a list of sorted images
    sorted_images = []
    # Iterate through the list of images
    for image in images:
        # Load the image
        image = Image.open(image)
        # Resize the image
        image = image.resize((224, 224))
        # Convert the image to a tensor
        image = torch.tensor(image)
        # Add a dimension to the tensor
        image = image.unsqueeze(0)
        # Normalize the image
        image = image / 255
        # Make a prediction
        with torch.no_grad():
            prediction = model(image)
        # Get the index of the prediction
        index = torch.argmax(prediction).item()
        # Create a list of folders
        folders = ['Animals', 'Landscapes', 'Objects']
        # Create a list of folders that don't exist
        new_folders = []
        for folder in folders:
            if not os.path.exists(folder):
                os.mkdir(folder)
        # Save the image into the correct folder
        pil_image = Image.fromarray(image)
        pil_image.save(folders[index] + '/' + image)
        # Delete the image from the directory
        os.remove(image)
        # Add the image to the list of sorted images
        sorted_images.append(image)
    return sorted_images

def humansort(sorted_images):
    for image in sorted_images:
        # Load the jpg file into a numpy array
        human_images = []
        image = face_recognition.load_image_file(image)
        # Find all the faces in the image
        face_locations = face_recognition.face_locations(image)
        
        # If there no faces ignore it, if there's once face sort it into a folder with that person's integer
        # If there's more than one face sort it into a folder for group photos
        if len(face_locations) == 0:
            pass
        elif len(face_locations) == 1:
            human_images.append(image)
            # Delete the image from the directory
            os.remove(image)
        else:
            # Create a folder for group photos if it doesn't exist
            if not os.path.exists('Group Photos'):
                os.makedirs('Group Photos')
            # Save the image into the group photos folder
            pil_image = Image.fromarray(image)
            pil_image.save('Group Photos/' + image)
            # Delete the image from the directory
            os.remove(image)
    return human_images

def recognize_faces(human_images):
    for image in human_images:
        # Load the jpg file into a numpy array
        image = face_recognition.load_image_file(image)
        # Find all the faces in the image
        face_locations = face_recognition.face_locations(image)
        
        # We already know that all these photos only have one face in them
        # so we can just take the first face and recognize it
        face_encoding = face_recognition.face_encodings(image)[0]
        # Load the known faces
        known_faces = []
        for filename in os.listdir('Known Faces'):
            known_faces.append(face_recognition.load_image_file(filename))
        # Compare the faces
        results = face_recognition.compare_faces(known_faces, face_encoding)
        # Create a list of names
        names = []
        for i in range(len(results)):
            if results[i]:
                names.append(os.listdir('Known Faces')[i])
        # If there's no match, create a new folder for the person
        if len(names) == 0:
            # Create a folder for the person
            os.makedirs('Known Faces/' + input('Enter the name of the person in the photo: '))
            # Save the photo in the folder
            pil_image = Image.fromarray(image)
            pil_image.save('Known Faces/' + input('Enter the name of the person in the photo: ') + '/' + image)
            # Delete the image from the directory
            os.remove(image)
        # If there's one match, save the photo in the folder
        elif len(names) == 1:
            # Save the photo in the folder
            pil_image = Image.fromarray(image)
            pil_image.save('Known Faces/' + names[0] + '/' + image)
            # Delete the image from the directory
            os.remove(image)
        # There should never be more than one match
        else:
            print('There was more than one match')
            return 1
    return 0
        

# Now I need a main function
def main():
    # We need to get the directory of the photos we want to convert
    directory = sys.argv[1]
    images = load_images(directory)
    convert_heic_to_jpg(images)
    
    # Now we're going to use machine learning to sort the photos into folders
    # based on the content in the photos, to achieve this we will use the
    # pytorch library
    sorted_images = sort(images)

    # Function extracting the human images from the photos
    human_images = humansort(sorted_images)

    # Finally we'll take all the photos with people in them and sort them
    # into folders based on the people in the photos
    recognize_faces(human_images)

    return 0
