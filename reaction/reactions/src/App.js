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
  }
  start_count() {
    // TODO: Your code here!
    this.setState({start_time: window.performance.now()});
    let duration = Math.floor(5 * Math.random()) + 2;
    this.setState({true_duration: duration});
    this.setState({counting: true});
    this.setState({color: 'darkred'});
    // Using "duration" prevents the bug where state change time is too slow.
    setTimeout(() => {this.setState({color: 'green'});}, duration * 1000);
  }
  end_count() {
    // TODO: Your code here!
    let current_time_ms = window.performance.now()
    if (current_time_ms > this.state.true_duration * 1000 + this.state.start_time)
    {
      this.setState({counting: false});
      this.setState({ran_once: true});
      this.setState({reaction_time: current_time_ms - this.state.true_duration * 1000 - this.state.start_time});
    }
  }
  process_click() {
    if (this.state.counting) {
      this.end_count();
    } else this.start_count();
  }
  render() {
    let msg = "";
    // TODO: Your code here!
    // If this.state.counting and the button is red, msg is Wait for Green.
    // If this.state.counting and the button is green, msg is Click!.
    // Otherwise, if you have ran once, msg is Your reaction time is {this.state.reaction_time} ms.
    // Otherwise, we have never run the test. So, msg is Click me to begin!

    if (this.state.counting)
    {
      if (this.state.color === 'darkred')
      {
        msg = "Wait for Green.";
      }
      else
      {
        msg = "Click Away!";
      }
    }
    else
    {
      if (this.state.ran_once)
      {
        msg = `Your reaction time is ${this.state.reaction_time.toFixed(2)} ms.`;
      }
      else 
      {
        msg = "Click me to begin!";
      }
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
