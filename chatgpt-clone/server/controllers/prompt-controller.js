const InputPrompt = require("../models/input-prompt");
const openai = require("../config/openai");
module.exports = {
    async sendText(req, res) {
        const OpenAI =  openai.configuration();
        const inputModel = new InputPrompt(req.body);
        try {
            const response = await OpenAI.createCompletion(openai.textCompletion(InputPrompt));
            res.status(200).json({
                sucess: true,
                data: response.data.choices[0].text
        })
            
        }catch (error) {
            return res.status(400).json({ 
                sucess: false,
                error: error.response  ? error.data : "Server Error"
            });    
        }
    }
}
