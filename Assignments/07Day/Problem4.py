import time
import logging
from datetime import datetime
from abc import ABC, abstractmethod
from contextlib import contextmanager
from functools import wraps

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Starting execution of {func.__name__}")
        result = func(*args, **kwargs)
        logging.info(f"Completed execution of {func.__name__}")
        return result
    return wrapper


def time_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logging.info(f"{func.__name__} executed in {execution_time:.4f} seconds")
        return result
    return wrapper


def validate_data(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if not hasattr(self, 'data') or not self.data:
            raise ValueError("Report data is empty or not set")
        logging.info(f"Data validation passed for {func.__name__}")
        return func(self, *args, **kwargs)
    return wrapper


class ReportFileManager:
    def __init__(self, filename, mode='w'):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        logging.info(f"Opening file: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
            logging.info(f"Closed file: {self.filename}")
        if exc_type is not None:
            logging.error(f"Error occurred: {exc_val}")
        return False


@contextmanager
def report_generation_context(report_name):
    logging.info(f"=" * 60)
    logging.info(f"Starting report generation: {report_name}")
    logging.info(f"=" * 60)
    start_time = time.time()
    
    try:
        yield
    except Exception as e:
        logging.error(f"Error during report generation: {e}")
        raise
    finally:
        end_time = time.time()
        logging.info(f"Report generation completed in {end_time - start_time:.4f} seconds")
        logging.info(f"=" * 60)


class ReportGenerator(ABC):
    def __init__(self, data):
        self.data = data
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    @abstractmethod
    def generate_content(self):
        pass
    
    @abstractmethod
    def save(self, filename):
        pass


class TextReport(ReportGenerator):
    def generate_content(self):
        yield f"TEXT REPORT\n"
        yield f"Generated: {self.timestamp}\n"
        yield f"{'-' * 50}\n"
        
        for i, line in enumerate(self.data, 1):
            yield f"{i}. {line}\n"
        
        yield f"{'-' * 50}\n"
        yield f"Total lines: {len(self.data)}\n"
    
    @log_execution
    @time_execution
    @validate_data
    def save(self, filename):
        with report_generation_context("Text Report"):
            with ReportFileManager(f"{filename}.txt") as file:
                for chunk in self.generate_content():
                    file.write(chunk)
                    time.sleep(0.01)
        
        logging.info(f"Text report saved: {filename}.txt")


class CSVReport(ReportGenerator):
    def __init__(self, data, headers=None):
        super().__init__(data)
        self.headers = headers or ["ID", "Value"]
    
    def generate_content(self):
        yield ",".join(self.headers) + "\n"
        
        for i, item in enumerate(self.data, 1):
            if isinstance(item, (list, tuple)):
                yield ",".join(map(str, item)) + "\n"
            else:
                yield f"{i},{item}\n"
    
    @log_execution
    @time_execution
    @validate_data
    def save(self, filename):
        with report_generation_context("CSV Report"):
            with ReportFileManager(f"{filename}.csv") as file:
                for chunk in self.generate_content():
                    file.write(chunk)
                    time.sleep(0.01)
        
        logging.info(f"CSV report saved: {filename}.csv")


class JSONReport(ReportGenerator):
    def generate_content(self):
        yield "{\n"
        yield f'  "report_type": "JSON Report",\n'
        yield f'  "timestamp": "{self.timestamp}",\n'
        yield f'  "data": [\n'
        
        for i, item in enumerate(self.data):
            if isinstance(item, dict):
                yield f"    {item}"
            else:
                yield f'    {{"id": {i+1}, "value": "{item}"}}'
            
            if i < len(self.data) - 1:
                yield ",\n"
            else:
                yield "\n"
        
        yield "  ]\n"
        yield "}\n"
    
    @log_execution
    @time_execution
    @validate_data
    def save(self, filename):
        with report_generation_context("JSON Report"):
            with ReportFileManager(f"{filename}.json") as file:
                for chunk in self.generate_content():
                    file.write(chunk)
                    time.sleep(0.01)
        
        logging.info(f"JSON report saved: {filename}.json")


class HTMLReport(ReportGenerator):
    def generate_content(self):
        yield "<!DOCTYPE html>\n"
        yield "<html>\n<head>\n"
        yield "  <title>Report</title>\n"
        yield "  <style>\n"
        yield "    body { font-family: Arial, sans-serif; margin: 20px; }\n"
        yield "    h1 { color: #333; }\n"
        yield "    table { border-collapse: collapse; width: 100%; }\n"
        yield "    th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }\n"
        yield "    th { background-color: #4CAF50; color: white; }\n"
        yield "  </style>\n"
        yield "</head>\n<body>\n"
        yield "  <h1>HTML Report</h1>\n"
        yield f"  <p>Generated: {self.timestamp}</p>\n"
        yield "  <table>\n"
        yield "    <tr><th>ID</th><th>Value</th></tr>\n"
        
        for i, item in enumerate(self.data, 1):
            yield f"    <tr><td>{i}</td><td>{item}</td></tr>\n"
        
        yield "  </table>\n"
        yield "</body>\n</html>\n"
    
    @log_execution
    @time_execution
    @validate_data
    def save(self, filename):
        with report_generation_context("HTML Report"):
            with ReportFileManager(f"{filename}.html") as file:
                for chunk in self.generate_content():
                    file.write(chunk)
                    time.sleep(0.01)
        
        logging.info(f"HTML report saved: {filename}.html")


class MarkdownReport(ReportGenerator):
    def generate_content(self):
        yield "# Markdown Report\n\n"
        yield f"**Generated:** {self.timestamp}\n\n"
        yield "---\n\n"
        yield "## Data\n\n"
        
        for i, item in enumerate(self.data, 1):
            yield f"{i}. {item}\n"
        
        yield f"\n---\n"
        yield f"**Total Items:** {len(self.data)}\n"
    
    @log_execution
    @time_execution
    @validate_data
    def save(self, filename):
        with report_generation_context("Markdown Report"):
            with ReportFileManager(f"{filename}.md") as file:
                for chunk in self.generate_content():
                    file.write(chunk)
                    time.sleep(0.01)
        
        logging.info(f"Markdown report saved: {filename}.md")


def data_generator(size=100):
    logging.info(f"Generating {size} data items...")
    for i in range(size):
        yield f"Data item {i+1}: Sample content for testing generators"


class ReportFactory:
    @staticmethod
    def create_report(report_type, data, **kwargs):
        report_types = {
            'TEXT': TextReport,
            'CSV': CSVReport,
            'JSON': JSONReport,
            'HTML': HTMLReport,
            'MARKDOWN': MarkdownReport
        }
        
        report_class = report_types.get(report_type.upper())
        if not report_class:
            raise ValueError(f"Unsupported report type: {report_type}")
        
        if report_type.upper() == 'CSV':
            return report_class(data, kwargs.get('headers'))
        
        return report_class(data)


def display_menu():
    print("\n" + "="*60)
    print("ADVANCED REPORT GENERATION SYSTEM")
    print("="*60)
    print("\nAvailable Report Types:")
    print("  1. Text Report")
    print("  2. CSV Report")
    print("  3. JSON Report")
    print("  4. HTML Report")
    print("  5. Markdown Report")
    print("  6. Demo Mode (Generate All Reports)")
    print("  7. Exit")
    print("="*60)


def main():
    while True:
        display_menu()
        
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == '7':
            print("\nThank you for using Report Generation System!")
            break
        
        if choice == '6':
            demo_mode()
            continue
        
        report_map = {
            '1': 'TEXT',
            '2': 'CSV',
            '3': 'JSON',
            '4': 'HTML',
            '5': 'MARKDOWN'
        }
        
        if choice not in report_map:
            print("\n❌ Invalid choice! Please try again.")
            continue
        
        report_type = report_map[choice]
        
        print(f"\n--- Creating {report_type} Report ---")
        
        data_choice = input("Use sample data? (y/n): ").strip().lower()
        
        if data_choice == 'y':
            size = int(input("Enter number of items (default 10): ").strip() or "10")
            data = list(data_generator(size))
        else:
            data = []
            print("Enter data items (type 'done' to finish):")
            while True:
                item = input("  > ").strip()
                if item.lower() == 'done':
                    break
                if item:
                    data.append(item)
        
        if not data:
            print("\n❌ No data provided!")
            continue
        
        filename = input("Enter filename (without extension): ").strip()
        
        if not filename:
            filename = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        try:
            kwargs = {}
            if report_type == 'CSV':
                headers_input = input("Enter CSV headers (comma-separated, or press Enter for default): ").strip()
                if headers_input:
                    kwargs['headers'] = [h.strip() for h in headers_input.split(',')]
            
            report = ReportFactory.create_report(report_type, data, **kwargs)
            report.save(filename)
            print(f"\n✓ Report generated successfully!")
            
        except Exception as e:
            print(f"\n❌ Error generating report: {e}")


def demo_mode():
    print("\n" + "="*60)
    print("DEMONSTRATION MODE")
    print("="*60)
    
    sample_data = list(data_generator(5))
    
    print("\n--- Generating All Report Types ---\n")
    
    reports = [
        ('TEXT', TextReport(sample_data), 'demo_text'),
        ('CSV', CSVReport(sample_data), 'demo_csv'),
        ('JSON', JSONReport(sample_data), 'demo_json'),
        ('HTML', HTMLReport(sample_data), 'demo_html'),
        ('MARKDOWN', MarkdownReport(sample_data), 'demo_markdown')
    ]
    
    for report_type, report, filename in reports:
        try:
            print(f"\nGenerating {report_type} report...")
            report.save(filename)
        except Exception as e:
            print(f"Error: {e}")
    
    print("\n" + "="*60)
    print("PYTHON FEATURES DEMONSTRATED")
    print("="*60)
    print("\n1. Generators:")
    print("   - generate_content() yields data lazily")
    print("   - data_generator() creates test data efficiently")
    print("   - Memory-efficient for large datasets")
    
    print("\n2. Decorators:")
    print("   - @log_execution: Logs function execution")
    print("   - @time_execution: Measures execution time")
    print("   - @validate_data: Validates data before processing")
    
    print("\n3. Context Managers:")
    print("   - ReportFileManager: Manages file resources")
    print("   - report_generation_context: Tracks report generation")
    print("   - Ensures proper cleanup and resource management")
    
    print("\n4. OOP Principles:")
    print("   - Abstract base class (ReportGenerator)")
    print("   - Inheritance (TextReport, CSVReport, etc.)")
    print("   - Polymorphism (different generate_content() implementations)")
    
    print("\n" + "="*60)


if __name__ == "__main__":
    main()
