import * as React from "react"

const Button = React.forwardRef(({ className, ...props }, ref) => {
  return (
    <button
      className="inline-flex items-center justify-center rounded-md text-sm font-medium bg-blue-600 text-white h-10 px-4 py-2 hover:bg-blue-700"
      ref={ref}
      {...props}
    />
  )
})
Button.displayName = "Button"

export { Button }
