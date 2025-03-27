import React, { useState } from 'react';
import { View, Text, Button, TextInput } from 'react-native';

export default function App() {
    const [thought, setThought] = useState('');
    const [response, setResponse] = useState('');

    const sendThought = async () => {
        try {
            const res = await fetch('http://127.0.0.1:8000/process-thought/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ thought }),
            });
            const data = await res.json();
            setResponse(data.organized_thought);
        } catch (error) {
            setResponse('Error processing thought');
        }
    };

    return (
        <View style={{ padding: 20 }}>
            <Text>Speak or type your thought:</Text>
            <TextInput
                value={thought}
                onChangeText={setThought}
                placeholder="Enter thought here"
                style={{ borderWidth: 1, padding: 10, marginBottom: 10 }}
            />
            <Button title="Organize Thought" onPress={sendThought} />
            {response ? <Text>Organized Thought: {response}</Text> : null}
        </View>
    );
}
