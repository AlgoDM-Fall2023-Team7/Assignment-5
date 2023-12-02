# Fashion Image Annotation and Retrieval System

## Part 1: Image Annotation Pipeline

### Task 1: Review and Generate Tags

Review the navigation bar from fashion retailers like Macy's and Amazon for image annotation. Generated tags include:

1. Apparel Type
2. Color
3. Pattern
4. Material
5. Occasion
6. Brand
7. Gender
8. Size
9. Style
10. Season

Create a JSON template for annotations with attributes such as image ID, and annotations for each tag. Write a prompt to collect image annotations using the OpenAI GPT-4 Vision API. Implement a pipeline script that generates annotations for images in an S3 bucket and upserts them into Snowflake.
## Part 2: Multi-Modal Retrieval Model

Refer to [2] for a multi-modal retrieval model using GPT-4 Vision.

## Part 3: Streamlit App for Retrieval System

Build a Streamlit app using the Streamlit library in Python. Refer to the Streamlit documentation for creating a user interface. The app should allow users to:

1. Search for similar images given an input image.
2. Search for images based on a text description.

Integrate the multi-modal retrieval model from Part 2 into the Streamlit app.

### References:

1. [GPT-4 Vision Product Tagging Implementation](https://github.com/petergpt/GPT4_Vision_Product_Tagging/blob/main/main.py)
2. [Multi-Modal Retrieval Model Example](https://github.com/run-llama/llama_index/blob/main/docs/examples/multi_modal/gpt4v_multi_modal_retrieval.ipynb)


## Project Contributions 

Aishwarya: 
1. Tag Generation and Review: Reviewed navigation bars on fashion retail websites like Macy's and Amazon. Generated a comprehensive list of at least 10 annotations or tags relevant to fashion products.
2. JSON Template Creation: Created a JSON template for the generated annotations, ensuring a structured and standardized format.
3. ChatGPT Prompt: Developed a prompt for ChatGPT to create JSON data for an image, enabling efficient annotation generation.

Arjun: 
1. GPT-4 Vision API Script: Utilized the OpenAI GPT-4 Vision API to build a robust script.
2. Implemented an automation pipeline to generate annotations for each image in an Amazon S3 bucket.
3. Multi-Modal Retrieval Model: Successfully developed a multi-modal retrieval model that, given an image, identifies other similar images and their associated text tags. Implemented the functionality to find images matching a given text string description.

Sanidhya: 
1. Streamlit App Development: Constructed a Streamlit app as the interface for the project.
2. Integrated the multi-modal retrieval model developed by Arjun into the Streamlit app for seamless interaction.
3. Collaboration and Integration: Collaborated closely with Arjun to ensure smooth integration of the multi-modal retrieval model into the Streamlit app.
4. Ensured a user-friendly interface and a cohesive user experience for both image and text-based searches.
