import React from 'react';
import './Home.css'
let games = [
    {
        teamNameRight: "Milwaukee Bucks",
        teamNameLeft: "Houston Rockets",
        Winner: "left"
    },    
    {
        teamNameRight: "LA Clippers",
        teamNameLeft: "Washington Wizards",
        Winner: "left"
    },
    {
        teamNameRight: "Dallas Mavericks",
        teamNameLeft: "New Orleans Pelicans",
        Winner: "left"
    },
    {
        teamNameRight: "Los Angeles Lakers",
        teamNameLeft: "Portland Trail Blazers",
        Winner: "left"
    },
    {
        teamNameRight: "Minnesota Timberwolves",
        teamNameLeft: "San Antonio Spurs",
        Winner: "left"
    },
    {
        teamNameRight: "Boston Celtics",
        teamNameLeft: "Toronto Raptors",
        Winner: "left"
    },
    {
        teamNameRight: "Memphis Grizzlies",
        teamNameLeft: "Phoenix Suns",
        Winner: "left"
    },
    {
        teamNameRight: "Miami Heat",
        teamNameLeft: "Atlanta Hawks",
        Winner: "left"
    },
    {
        teamNameRight: "Utah Jazz",
        teamNameLeft: "Brooklyn Nets",
        Winner: "left"
    },
    {
        teamNameRight: "Oklahoma City Thunder",
        teamNameLeft: "Denver Nuggets",
        Winner: "left"
    },
    {
        teamNameRight: "Philadelphia 76ers",
        teamNameLeft: "Indiana Pacers",
        Winner: "left"
    }
]
export default function Home() {
    return <div className='gameList'>
        {
            games.map((game, index)=>{
                return (
                    <div className={index!==games.length-1 ? "game" : "game last"}>
                        <div className='teamLeft'>{game.teamNameLeft}</div>
                        <div className='teamRight'>{game.teamNameRight}</div>
                    </div>
                )
            })
        }
    </div>;
}