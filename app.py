import { useState } from "react";
import { Button } from "@/components/ui/button";

export default function Home() {
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    if (!selectedFile) return;
    const formData = new FormData();
    formData.append("file", selectedFile);

    const response = await fetch("/api/upload", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();
    console.log("Uploaded file:", data);
  };

  return (
    <div className="flex flex-col items-center p-6">
      <h1 className="text-2xl font-bold">PDF Converter</h1>
      <input type="file" accept="application/pdf" onChange={handleFileChange} className="my-4" />
      <Button onClick={handleUpload} disabled={!selectedFile}>
        Upload & Convert
      </Button>
    </div>
  );
}
