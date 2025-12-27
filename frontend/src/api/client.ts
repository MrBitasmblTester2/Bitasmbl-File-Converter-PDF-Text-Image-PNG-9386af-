export async function convertFile(file: File){
  const formData = new FormData();
  formData.append("file", file);
  const res = await fetch("/convert",{method:"POST",body:formData});
  if(!res.ok) throw new Error("Convert failed");
  return res.json();
}