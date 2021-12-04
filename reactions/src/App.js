import logo from './logo.svg';
import './App.css';
import React from 'react';

class Panel extends React.Component {
  constructor(props) {
    super(props);
    this.state = { start_time:0, ran_once:false, counting:false, true_duration:0, reaction_time:0, color:'green' };
    this.process_click = this.process_click.bind(this);
  }
  handle_color = (c) => {
    // TODO: Your code here!
  }
  start_count() {
    // TODO: Your code here!
    let time = (2 + Math.random() * 5) * 1000;
    this.setState({ start_time:window.performance.now(), true_duration:time, counting:true, color:'darkred' });
    setTimeout(() => { this.setState({ color:'green' }); }, time);
  }
  end_count() {
    // TODO: Your code here!
    const elapsed_time = window.performance.now() - this.state.start_time;
    if(elapsed_time > this.state.true_duration){
      this.setState({ ran_once: true, counting: false, reaction_time: elapsed_time - this.state.true_duration});
    }
  }
  process_click() {
    if (this.state.counting) {
      this.end_count();
    } else this.start_count();
  }
  render() {
    let msg = "";
    if(this.state.counting && this.state.color === 'darkred'){
      msg = "Wait for Green";
    }
    else if(this.state.counting && this.state.color === 'green'){
      msg = "Click!";
    }
    else if(this.state.ran_once){
      msg = 'Your reaction time is ' + this.state.reaction_time + ' ms';
    }
    else{
      msg = "Click me to begin!";
    }
    // TODO: Your code here!
    return (
      <div className = "PanelContainer" onClick = {this.process_click} style={ { background: this.state.color} }>
        <div className = "Panel">{msg}</div>
      </div>
    );
  }
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1 className =  "Header">How Fast is your Reaction Time?</h1>
        <Panel />
        <p>Click as soon as the red box turns green. Click anywhere in the box to start.</p>
      </header>
    </div>
  );
}
export default App;