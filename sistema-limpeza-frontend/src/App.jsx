import { useState } from 'react'
import { Button } from './components/ui/button'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <h1 className="text-3xl font-bold text-blue-600 mb-4">
        Sistema de Gestão de Limpeza
      </h1>
      <p className="text-gray-700 mb-8">
        O seu sistema está online e pronto para ser configurado!
      </p>
      <Button onClick={() => setCount((count) => count + 1)}>
        Teste de Botão: {count}
      </Button>
      <div className="mt-8 p-4 bg-white rounded shadow">
        <p className="text-sm text-gray-500">
          Status do Backend: <span className="text-green-500 font-bold">Conectado</span>
        </p>
      </div>
    </div>
  )
}

export default App
