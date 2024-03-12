import React,{useState}from 'react';
import PropTypes from 'prop-types';



export default function TextForm(props) {
    const [text,setText] = useState("Enter text here");
    const handleOnChange =(event)=>{
        setText(event.target.value);

    };
    const handleUpClick =()=>{
        let newText = text.toUpperCase();
        setText(newText);
    };
    const handledwClick =()=>{
        let newText = text.toLowerCase();
        setText(newText);
    }
  return (
    <>
      <div>
        <h2>{props.heading}</h2>
        <br />
        <div className="TextArea">
          <div className="form-floating">
            <textarea
              className="form-control"
              value={text}
              placeholder="Leave a comment here"
              id="floatingTextarea2" onChange={handleOnChange}
              style={{ height: 'auto', border: '1px solid black' }}
              rows={15}
            ></textarea>
          </div>
        </div>
        <br />
        <button id="uppercase" type="button" className="btn btn-primary" onClick={handleUpClick}>
          Convert to Uppercase
        </button>
   
        <button id="uppercase" type="button" className="btn btn-primary" onClick={handledwClick} style={{marginLeft:'20px'}}>
          Convert to Lowercase
        </button>
      </div>
      <div className='container my-4'>
        <h1>Your text summary</h1>
        <p>Number of words :{text.split(" ").length}</p>
        <p>Number of Characters: {text.length}</p>
        <p>Reading time : {0.08*text.split(" ").length} minutes</p>
        <h3>Preview</h3>
        <p>{text}</p>
      </div>
    </>
  );
}

TextForm.propTypes = {
  heading: PropTypes.string.isRequired,
};


