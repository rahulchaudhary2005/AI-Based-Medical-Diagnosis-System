from fastai.text.all import *
import gradio as gr


learn = load_learner('model.pkl')


description = "Medical Diagnosis"
categories = (['Allergy', 'Anemia', 'Bronchitis', 'Diabetes', 'Diarrhea', 'Fatigue', 'Flu', 'Malaria', 'Stress'])



def classify_text(txt):
    pred,idx,probs = learn.predict(txt)
    return dict(zip(categories, map(float,probs)))



text = gr.Textbox(lines=2, label='Describe how you feel in great detail')
label = gr.Label()
examples = ['I have no intrest in physical activity. i am always thirsty', 'I am freezing', 'My eyes are pale']

intf = gr.Interface(fn=classify_text, inputs=text, outputs=label, examples=examples, description=description)
intf.launch(inline=False)





