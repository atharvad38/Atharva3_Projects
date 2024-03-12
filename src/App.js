import logo from './logo.svg';
import './App.css';
import NavBar from './components/NavBar';
import About from './components/About';
import TextForm from './components/TextForm';

function App() {
  return (
   <>
   {/*<NavBar title="TextUtils"/>*/}
   <NavBar title="TextUtils"/>
   <br></br>
   <div className="container">
   {/*<TextForm heading="Enter Text to analyze"/>*/}
   <About/>
   </div>
   
   </>
  );
}

export default App;
