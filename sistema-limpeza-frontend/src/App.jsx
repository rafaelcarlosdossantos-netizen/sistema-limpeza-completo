import { useState } from 'react'
import { Button } from '@/components/ui/button'

function App() {
  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center justify-center p-4">
      <div className="max-w-md w-full bg-white rounded-lg shadow-xl p-8">
        <h1 className="text-2xl font-bold text-center text-blue-600 mb-6">
          Sistema de Gestão de Limpeza
        </h1>
        
        <div className="space-y-4">
          <p className="text-gray-600 text-center">
            Bem-vindo ao seu novo sistema de gestão.
          </p>
          
          <div className="grid grid-cols-1 gap-4">
            <Button className="w-full">Acessar Painel</Button>
            <Button variant="outline" className="w-full">Configurações</Button>
          </div>
        </div>
        
        <div className="mt-8 pt-6 border-t border-gray-200">
          <p className="text-xs text-center text-gray-400">
            Status do Servidor: <span className="text-green-500">Online</span>
          </p>
        </div>
      </div>
    </div>
  )
}

export default App
