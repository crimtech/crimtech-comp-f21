//import logo from './logo.svg';
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
    this.setState({start_time: window.performance.now(), true_duration: Math.floor(Math.random() * (6)) + 2, counting: true, color: 'red'})
    this.set_green()
  }
  end_count() {
    // TODO: Your code here!
    var time = window.performance.now() - this.state.start_time;
    if(time > this.state.true_duration)
    {
      this.setState({ran_once: true, counting: false, reaction_time: time - this.state.true_duration})
    }
  }
  set_green() {
    setTimeout(() => this.setState({color: 'green'}), this.state.true_duration*1000)
  }
  process_click() {
    if (this.state.counting) {
      this.end_count();
    } else this.start_count();
  }
  render() {
    var msg = "Hello World!";

    // TODO: Your code here!
    if(this.state.counting)
    {
      if(this.state.color === 'dark red')
      {
        msg = "Wait for Green";
      }
      else
      {
        msg = "Click!";
      }
    }
    else if(this.state.ran_once)
    {
      msg = `Your reaction time is ${this.state.reaction_time} ms`;
    }
    else
    {
      msg = "Click me to begin!";
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
