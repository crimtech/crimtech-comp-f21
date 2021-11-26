import logo from './logo.svg';
import './App.css';
import React from 'react';

class Panel extends React.Component {
  constructor(props) {
    super(props);
    this.state = {start_time: 0, ran_once: false, counting: false, true_duration:Math.random() * 5000 + 2000, reaction_time: 0, color: "green"};
    this.process_click = this.process_click.bind(this);
  }
  handle_color = (c) => {
    setTimeout(() => 
      this.setState({color:c}),
      this.state.true_duration);
  }
  start_count() {
    this.setState({start_time:window.performance.now()});
    this.setState({true_duration:Math.random() * 5000 + 2000});
    this.setState({color:"darkred"}, () =>
      this.handle_color("green"));
    this.setState({counting:true});
  }
  end_count() {
    if (window.performance.now() > this.state.start_time + this.state.true_duration){
      this.setState({ran_once:true});
      this.setState({counting:false});
      this.setState({reaction_time:window.performance.now() - this.state.start_time - this.state.true_duration});
    }
  }
  process_click() {
    if (this.state.counting) {
      this.end_count();
    } else this.start_count();
  }
  render() {
    console.log("rendering");
    console.log(this.state.color);
    console.log(this.state.counting);
    let msg = "Click me to begin!";
    if (this.state.counting && this.state.color === "darkred") {
      msg = "Wait for Green.";
    } else if (this.state.counting && this.state.color === "green") {
      msg = "Click!";
    } else if (this.state.ran_once) {
      msg = `Your reaction time is ${this.state.reaction_time} ms!`;
    }
    return (
      <div className = "PanelContainer" onClick = {this.process_click} style={{background: this.state.color} }>
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
        <Panel/>
        <p>Click as soon as the red box turns green. Click anywhere in the box to start.</p>
      </header>
    </div>
  );
}

export default App;
