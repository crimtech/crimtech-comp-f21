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
    console.log("true duration: " + this.state.true_duration);
    setTimeout(() => {this.setState({color: c})}, this.state.true_duration * 1000);
  }
  start_count() {
    const time_now = window.performance.now();
    const rand_c = Math.floor(Math.random() * 5 + 2);
    this.setState({start_time: time_now, counting: true, color: "#8B0000"});
    this.setState({true_duration: rand_c},
      () => {
        this.handle_color("green");
      });
  }
  end_count() {
    const time_now = window.performance.now();
    const duration = this.state.true_duration;
    console.log("end_count()");
    console.log(time_now);
    if (time_now > duration * 1000 + this.state.start_time) {
      const time = (time_now - this.state.start_time - (duration * 1000))/1000;
      this.setState({ran_once: true, counting: false, reaction_time: time, color: "green"});
    }
  }
  process_click() {
    if (this.state.counting) {
      this.end_count();
    } else this.start_count();
  }
  render() {
    let msg = "Click me to begin!";
    const count = this.state.counting;
    console.log(count);
    if (count) {
      msg = "Please wait for green!";
    }
    if (count && this.state.color == "green") {
      msg = "Click now!";
    }
    if (this.state.ran_once) {
      msg = "Your reaction time is " + this.state.reaction_time +" seconds.";
    }
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
