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
