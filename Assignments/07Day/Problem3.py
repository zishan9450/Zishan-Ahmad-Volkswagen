from abc import ABC, abstractmethod
from datetime import datetime


class ReportGenerator(ABC):
    def generate_report(self, data, filename):
        print(f"\n{'='*60}")
        print(f"Generating {self.__class__.__name__}")
        print(f"{'='*60}")
        
        parsed_data = self.parse(data)
        validated_data = self.validate(parsed_data)
        final_data = self.process(validated_data)
        self.save(final_data, filename)
        
        print(f"\n✓ Report generated successfully: {filename}")
        print(f"{'='*60}\n")
    
    @abstractmethod
    def parse(self, data):
        pass
    
    @abstractmethod
    def validate(self, data):
        pass
    
    @abstractmethod
    def process(self, data):
        pass
    
    @abstractmethod
    def save(self, data, filename):
        pass


class StandardReport(ReportGenerator):
    def parse(self, data):
        print("Step 1: Parsing data...")
        parsed = {"content": data, "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        print(f"  ✓ Parsed {len(data)} characters")
        return parsed
    
    def validate(self, data):
        print("Step 2: Validating data...")
        if not data.get("content"):
            raise ValueError("Content is empty")
        print("  ✓ Data validated successfully")
        return data
    
    def process(self, data):
        print("Step 3: Processing (Standard)...")
        return data
    
    @abstractmethod
    def save(self, data, filename):
        pass


class SpecialReport(ReportGenerator):
    def parse(self, data):
        print("Step 1: Parsing data...")
        parsed = {"content": data, "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        print(f"  ✓ Parsed {len(data)} characters")
        return parsed
    
    def validate(self, data):
        print("Step 2: Validating data...")
        if not data.get("content"):
            raise ValueError("Content is empty")
        print("  ✓ Data validated successfully")
        return data
    
    def revalidate(self, data):
        print("Step 3: Revalidating data (Special Report)...")
        if len(data.get("content", "")) < 10:
            print("  ⚠ Warning: Content is too short")
        print("  ✓ Data revalidated successfully")
        return data
    
    def process(self, data):
        return self.revalidate(data)
    
    @abstractmethod
    def save(self, data, filename):
        pass


class PDFReport(StandardReport):
    def save(self, data, filename):
        print(f"Step 4: Saving as PDF...")
        with open(f"{filename}.pdf", 'w') as f:
            f.write(f"PDF REPORT\n")
            f.write(f"Generated: {data['timestamp']}\n")
            f.write(f"Content:\n{data['content']}\n")
        print(f"  ✓ Saved to {filename}.pdf")


class DOCXReport(StandardReport):
    def save(self, data, filename):
        print(f"Step 4: Saving as DOCX...")
        with open(f"{filename}.docx", 'w') as f:
            f.write(f"DOCX REPORT\n")
            f.write(f"Generated: {data['timestamp']}\n")
            f.write(f"Content:\n{data['content']}\n")
        print(f"  ✓ Saved to {filename}.docx")


class TXTReport(StandardReport):
    def save(self, data, filename):
        print(f"Step 4: Saving as TXT...")
        with open(f"{filename}.txt", 'w') as f:
            f.write(f"TXT REPORT\n")
            f.write(f"Generated: {data['timestamp']}\n")
            f.write(f"Content:\n{data['content']}\n")
        print(f"  ✓ Saved to {filename}.txt")


class CSVReport(SpecialReport):
    def save(self, data, filename):
        print(f"Step 4: Saving as CSV...")
        with open(f"{filename}.csv", 'w') as f:
            f.write("Timestamp,Content\n")
            f.write(f"{data['timestamp']},{data['content']}\n")
        print(f"  ✓ Saved to {filename}.csv")


class JSONReport(SpecialReport):
    def save(self, data, filename):
        print(f"Step 4: Saving as JSON...")
        import json
        with open(f"{filename}.json", 'w') as f:
            json.dump(data, f, indent=2)
        print(f"  ✓ Saved to {filename}.json")


class ReportFactory:
    @staticmethod
    def create_report(report_type):
        report_types = {
            'PDF': PDFReport,
            'DOCX': DOCXReport,
            'TXT': TXTReport,
            'CSV': CSVReport,
            'JSON': JSONReport
        }
        
        report_class = report_types.get(report_type.upper())
        if not report_class:
            raise ValueError(f"Unsupported report type: {report_type}")
        
        return report_class()


def display_menu():
    print("\n" + "="*60)
    print("REPORT GENERATION SYSTEM")
    print("="*60)
    print("\nAvailable Report Types:")
    print("\nStandard Reports (Parse → Validate → Save):")
    print("  1. PDF Report")
    print("  2. DOCX Report")
    print("  3. TXT Report")
    print("\nSpecial Reports (Parse → Validate → Revalidate → Save):")
    print("  4. CSV Report")
    print("  5. JSON Report")
    print("\n  6. Exit")
    print("="*60)


def main():
    while True:
        display_menu()
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '6':
            print("\nThank you for using Report Generation System!")
            break
        
        report_map = {
            '1': 'PDF',
            '2': 'DOCX',
            '3': 'TXT',
            '4': 'CSV',
            '5': 'JSON'
        }
        
        if choice not in report_map:
            print("\n❌ Invalid choice! Please try again.")
            continue
        
        report_type = report_map[choice]
        
        print(f"\n--- Creating {report_type} Report ---")
        content = input("Enter report content: ").strip()
        
        if not content:
            print("\n❌ Content cannot be empty!")
            continue
        
        filename = input("Enter filename (without extension): ").strip()
        
        if not filename:
            filename = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        try:
            report = ReportFactory.create_report(report_type)
            report.generate_report(content, filename)
        except Exception as e:
            print(f"\n❌ Error generating report: {e}")


def demo_mode():
    print("\n" + "="*60)
    print("DEMONSTRATION MODE")
    print("="*60)
    
    test_data = "This is a sample report demonstrating the Template Method Pattern in Python."
    
    print("\n--- Standard Reports ---")
    
    pdf_report = PDFReport()
    pdf_report.generate_report(test_data, "demo_report_pdf")
    
    docx_report = DOCXReport()
    docx_report.generate_report(test_data, "demo_report_docx")
    
    txt_report = TXTReport()
    txt_report.generate_report(test_data, "demo_report_txt")
    
    print("\n--- Special Reports ---")
    
    csv_report = CSVReport()
    csv_report.generate_report(test_data, "demo_report_csv")
    
    json_report = JSONReport()
    json_report.generate_report(test_data, "demo_report_json")
    
    print("\n" + "="*60)
    print("DESIGN PATTERNS & OOP PRINCIPLES APPLIED")
    print("="*60)
    print("\n1. Template Method Pattern:")
    print("   - ReportGenerator defines the algorithm structure")
    print("   - Subclasses implement specific steps")
    
    print("\n2. Abstraction:")
    print("   - ABC (Abstract Base Class) for ReportGenerator")
    print("   - Abstract methods: parse(), validate(), process(), save()")
    
    print("\n3. Inheritance:")
    print("   - StandardReport and SpecialReport inherit from ReportGenerator")
    print("   - Concrete report types inherit from Standard/Special Reports")
    
    print("\n4. Polymorphism:")
    print("   - Different implementations of save() for each report type")
    print("   - Different process() behavior for Standard vs Special reports")
    
    print("\n5. Open/Closed Principle:")
    print("   - New report types can be added without modifying existing code")
    print("   - Just create a new class inheriting from StandardReport or SpecialReport")
    
    print("\n6. Factory Pattern:")
    print("   - ReportFactory creates appropriate report instances")
    
    print("\n" + "="*60)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        demo_mode()
    else:
        main()
