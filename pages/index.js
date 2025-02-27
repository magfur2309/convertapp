import Head from 'next/head';

export default function Home() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <Head>
        <title>PDF Converter</title>
      </Head>
      <h1 className="text-4xl font-bold">Welcome to PDF Converter</h1>
      <p className="text-lg text-gray-600">Convert your files easily</p>
    </div>
  );
}
