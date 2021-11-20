import logo from './logo.svg';
import './App.css';
import React from 'react';

class Panel extends React.Component {
  constructor(props) {
    super(props);
    this.state = { start_time: 0, ran_once: false, counting: false, true_duration: 0, reaction_time: 0, color: 'green'};
    this.process_click = this.process_click.bind(this);
  }
  handle_color = (c) => {
    // TODO: Your code here!
    console.log("true duration: " + this.state.true_duration);
    setTimeout(() => {this.setState({color: c})}, this.state.true_duration * 1000);
  }

  start_count() {
    // TODO: Your code here!
    const current_time = window.performance.now();
    const rand = Math.floor(Math.random() * 5 + 2);
    this.setState({start_time: current_time, counting: true, color: "#8B0000"});

    this.setState({true_duration: rand},
      () => {
        this.handle_color("green");
      }
    );
  }
  end_count() {
    // TODO: Your code here!
    console.log("end_count()");
    console.log(window.performance.now());
    if (window.performance.now() > this.state.true_duration * 1000 + this.state.start_time) {
      const time = (window.performance.now() - this.state.start_time - (this.state.true_duration * 1000))/1000;
      this.setState({ran_once: true, counting: false, reaction_time: time, color: "green"});
    }
    
  }
  process_click() {
    if (!this.state.ran_once) {
      if (this.state.counting) {
        this.end_count();
      } else {
        this.start_count();
      }
    }
  }
  render() {
    let msg = "Cick me to begin!";
    console.log(this.state.counting);
    if (this.state.counting) {
      msg = "Wait for Green";
    }
    if (this.state.counting && this.state.color == "green") {
      msg = "Click!";
    }
    if (this.state.ran_once) {
      msg = "Your reaction time is " + this.state.reaction_time +" seconds.";
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
