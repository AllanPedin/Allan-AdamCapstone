import React from 'react';
import './Home.css'
const axios = require('axios')
const constants = require("../constants")

export default class Home extends React.Component {
    state = {
      games: []
    }
    componentDidMount() {
        axios.get(constants.API_ENDPOINT+ "gamepredictions/").then((response)=>{
            console.log(response)
            let games = response.data.games;
            this.setState({ games });
        },(error)=>{
            console.log(error);
        })
    }
    render() {
        return <div className = 'gameList'>
        {
            this.state.games.map((game, index)=>{
                return (
                    <div className={index!==this.state.games.length-1 ? "game" : "game last"}>
                        <div className='teamLeft'>{game.teamName1}</div>
                        <div className="vs">vs</div>
                        <div className='teamRight'>{game.teamName2}</div>
                    </div>
                )
            })
        }
    </div>;
    }
  }