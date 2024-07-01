import React from "react";
import "./ChatMessage.css";
import Avatar from "../../assets/avatar";

//user(user or bot)
// //message -  prompt or response
// {
//     user:'gpt'
//     message:'Hello, how can I help you today?'
// }
export const ChatMessage = ({ message }) => {
    return(
        <div className={`chat-message ${message.user ==='gpt' && "chatgpt"}`}>
            <div className="chat-message-center">
                <div className={`avatar ${message.user ==='gpt' && "chatgpt"} `}>
                    {message.user==='gpt' && (<Avatar/>)}
                </div>
                <div className="message">
                    {message.message}
                </div>
            </div>
        </div>
    )
}