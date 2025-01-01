import { Wrench } from 'lucide-react';

export default function Maintenance() {
  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center justify-center p-4">
      <div className="text-center">
        <Wrench className="w-16 h-16 text-blue-500 mx-auto mb-4" />
        {/* eslint-disable-next-line react/no-unescaped-entities */}
        <h1 className="text-4xl font-bold text-gray-800 mb-2">We'll be right back!</h1>
        <p className="text-xl text-gray-600 mb-4">
          The Framework Patcher website is temporarily down for maintenance.
        </p>
        <p className="text-lg text-gray-500 mb-8">
          {/* eslint-disable-next-line react/no-unescaped-entities */}
          We're working on improving our services for you.
        </p>
        <p className="text-gray-600">
          If you have any urgent inquiries, please contact us at{' '}
          <a href="https://telegram.me/codes9488" className="text-blue-500 hover:underline">
            Codes9488
          </a>
        </p>
      </div>
    </div>
  );
}

