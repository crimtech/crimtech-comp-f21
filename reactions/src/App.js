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
    setTimeout(
      () => this.setState({ color: 'green'}), 
      this.state.true_duration * 1000
    );
  }
  //min = 2;
  //max = 7;
  start_count() {
    // TODO: Your code here!
    this.setState({counting:true, color:'#8b0000', start_time:window.performance.now()});
    const randomw = Math.floor(Math.random() * 7 + 1);
    this.setState({true_duration: randomw}, ()=> {this.handle_color("green")});
  }
  end_count() {
    // TODO: Your code here!
    if (window.performance.now() > this.state.true_duration * 1000 + this.state.start_time) {
      this.setState({counting:false, ran_once:true});
      const time = window.performance.now() - this.state.start_time - (this.state.true_duration * 1000);
      this.setState({reaction_time: Math.round(time)});
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
    let msg = "Click me to begin!";
    // TODO: Your code here!
    if (this.state.counting && this.state.color === 'red') {
      msg = "Wait for Green!";
    }
    if (this.state.counting && this.state.color === 'green') {
      msg = "Click!";
    }
    if (this.state.ran_once) {
      msg = "Your reaction time is" + this.state.reaction_time + "ms";
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
