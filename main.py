import streamlit as st
import json
from annotated_text import annotated_text

def save_annotations(text, annotations):
    """
    Save annotations to a JSON format.

    Args:
        text (str): The original text that was annotated.
        annotations (list): A list of annotation dictionaries, where each dictionary contains:
            - start_pos (int): The start position of the annotation in the text.
            - end_pos (int): The end position of the annotation in the text.
            - label (str): The label assigned to the annotated text.
            - text_fragment (str): The actual text that was annotated.

    Returns:
        str: A JSON-formatted string representing the annotated data.
    """
    annotated_data = {
        "text": text,
        "annotations": annotations
    }
    json_data = json.dumps(annotated_data, indent=4)
    return json_data

def get_annotated_text(text, annotations):
    """
    Create a list of text fragments with annotations highlighted for display.

    Args:
        text (str): The original text that was annotated.
        annotations (list): A list of annotation dictionaries, where each dictionary contains:
            - start_pos (int): The start position of the annotation in the text.
            - end_pos (int): The end position of the annotation in the text.
            - label (str): The label assigned to the annotated text.

    Returns:
        list: A list of tuples where each tuple contains a fragment of the text,
              the label, and a color code if the fragment is annotated. Unannotated
              fragments are included as strings without a label or color.
    """
    annotated_text_list = []
    last_end = 0
    
    for annotation in sorted(annotations, key=lambda x: x['start_pos']):
        start_pos = annotation['start_pos']
        end_pos = annotation['end_pos']
        label = annotation['label']

        # Append unannotated text
        if start_pos > last_end:
            annotated_text_list.append(text[last_end:start_pos])
        
        # Append annotated text
        annotated_text_list.append((text[start_pos:end_pos], label, "#8ef"))
        last_end = end_pos
    
    # Append remaining unannotated text
    if last_end < len(text):
        annotated_text_list.append(text[last_end:])
    
    return annotated_text_list

def paginate_text(text, indices_per_page):
    """
    Split the text into pages based on the specified number of characters per page.

    Args:
        text (str): The original text to paginate.
        indices_per_page (int): The number of characters per page.

    Returns:
        list: A list of strings, where each string represents a page of text.
    """
    pages = [text[i:i+indices_per_page] for i in range(0, len(text), indices_per_page)]
    return pages

def main():
    """
    Main function to run the Streamlit application for text annotation.
    
    The application allows users to upload a text file, view it in a paginated format, 
    annotate portions of the text, and download the annotations as a JSON file.
    
    Steps:
    1. Upload a text file.
    2. View the text in pages and annotate specific text fragments.
    3. Save and download the annotations as a JSON file.
    """
    st.title("Text Annotation Application Prototype")
    
    # Step 1: Text File Upload
    uploaded_file = st.file_uploader("Upload a text file", type=["txt"])
    
    if uploaded_file is not None:
        # Reading the uploaded file
        text = uploaded_file.getvalue().decode("utf-8")
        
        # Pagination
        indices_per_page = 25  # Number of characters per page
        pages = paginate_text(text, indices_per_page)
        num_pages = len(pages)
        
        st.write(f"### Uploaded Text (Total characters: {len(text)})")
        
        page_num = st.number_input("Select Page", min_value=1, max_value=num_pages, value=1)
        st.write(f"Showing page {page_num} of {num_pages}")

        current_page_text = pages[page_num - 1]
        start_index = (page_num - 1) * indices_per_page

        # Display only the current page's indexed text
        indexed_text = "\n".join([f"{i+start_index}: {char}" for i, char in enumerate(current_page_text)])
        st.text(indexed_text)
        
        # Initialize or load annotations
        if 'annotations' not in st.session_state:
            st.session_state['annotations'] = []
        
        annotations = st.session_state['annotations']
        annotated_text_list = get_annotated_text(text, annotations)
        st.write("### Annotated Text Preview")
        annotated_text(*annotated_text_list)
        
        # Step 2: Text Annotation
        st.write("### Annotate Text")
        
        start_pos = st.number_input("Start Position", min_value=0, max_value=len(text), value=0)
        end_pos = st.number_input("End Position", min_value=0, max_value=len(text), value=1)
        label = st.text_input("Label", value="PERSON")
        
        if st.button("Add Annotation"):
            if 0 <= start_pos < end_pos <= len(text):
                annotations.append({
                    "start_pos": start_pos,
                    "end_pos": end_pos,
                    "label": label,
                    "text_fragment": text[start_pos:end_pos]
                })
                st.session_state['annotations'] = annotations
                st.success("Annotation Added!")
            else:
                st.error("Invalid annotation positions.")
        
        # Display the annotated text with labels
        if annotations:
            st.write("### Current Annotations")
            annotated_text_list = get_annotated_text(text, annotations)
            annotated_text(*annotated_text_list)
        
        # Step 3: Save Annotations
        if annotations:
            st.write("### Save Annotations")
            json_data = save_annotations(text, annotations)
            st.download_button(
                label="Download Annotations as JSON",
                data=json_data,
                file_name="annotations.json",
                mime="application/json"
            )

if __name__ == "__main__":
    main()
