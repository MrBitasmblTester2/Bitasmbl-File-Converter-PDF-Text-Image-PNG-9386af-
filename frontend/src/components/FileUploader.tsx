import React from "react";
type Props={onSubmit:(file:File)=>void};
export function FileUploader({onSubmit}:Props){
  return <input type="file" onChange={()=>{}} />;
}