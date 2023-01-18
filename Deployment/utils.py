import pickle
import pytesseract
from PIL import Image
from pdf2image import convert_from_path
import re

def load_pkl(fname):
    """
    load pickle file
    """
    with open(fname, 'rb') as f:
        obj = pickle.load(f)
    return obj


def generate_one_hot_vec(inp_list,train_skills):

    """
    generate vector for skills
    """
    one_hot_dict = {i:0 for i in train_skills}

    for i in inp_list:
     if i in one_hot_dict.keys():
        one_hot_dict[i] = 1
    return list(one_hot_dict.values()), list(one_hot_dict.keys())



def similarity_jd(inp_skills,JD_SKILLS):
    """
    percentage of skills match with job description
    """
    count = 0 
    for i in inp_skills:
      if i in JD_SKILLS:
        count +=1
  
    return count/len(JD_SKILLS)



    
def convert_pdf_to_text(file_path="example.pdf"):
    """
    convert pdf to list of text
    """
    
    extracted_text = []
    images = convert_from_path(file_path)
    for image in images:
        print(image)
        text = pytesseract.image_to_string(image)
        text = re.sub(r'^$\n', '', text, flags=re.MULTILINE)
        extracted_text.append(text)
    
    extracted_text = ' '.join(extracted_text)
    return extracted_text

