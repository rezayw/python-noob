from flask import Flask, render_template, request, session
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY')

def initialize_session():
    """Initialize session arrays if not exists"""
    if 'original_array' not in session:
        session['original_array'] = []
        session['current_array'] = []

def process_array_input(input_str):
    """Process and validate array input string"""
    try:
        return [int(x.strip()) for x in input_str.split(',') if x.strip()]
    except ValueError:
        raise ValueError("Input must contain numbers only (e.g. '1,2,3')")

def perform_operations(request, results):
    """Handle all array operations"""
    # Update array if new input provided
    if 'array_data' in request.form and request.form['array_data'].strip():
        try:
            new_array = process_array_input(request.form['array_data'])
            session['original_array'] = new_array
            session['current_array'] = new_array.copy()
            results['message'] = "Array updated successfully"
        except ValueError as e:
            results['error'] = str(e)
            return

    # Array operations
    if not session['current_array']:
        results['error'] = "Array is empty"
        return

    if 'get_first' in request.form:
        results['first'] = session['current_array'][0]

    if 'get_last' in request.form:
        results['last'] = session['current_array'][-1]

    if 'get_max' in request.form:
        results['max'] = max(session['current_array'])

    if 'get_min' in request.form:
        results['min'] = min(session['current_array'])

    if 'get_even' in request.form:
        results['even'] = [x for x in session['current_array'] if x % 2 == 0]

    if 'get_odd' in request.form:
        results['odd'] = [x for x in session['current_array'] if x % 2 != 0]

    if 'slice_data' in request.form:
        try:
            start = int(request.form.get('start', 0))
            end = int(request.form.get('end', len(session['current_array'])))
            results['slice'] = session['current_array'][start:end]
            session['current_array'] = session['current_array'][start:end]
        except ValueError:
            results['error'] = "Invalid slice indices"

    if 'reset' in request.form:
        session['current_array'] = session['original_array'].copy()
        results['reset'] = True

@app.route('/', methods=['GET', 'POST'])
def index():
    """Main application route"""
    initialize_session()
    results = {}
    
    if request.method == 'POST':
        perform_operations(request, results)
    
    # Always include current array state in results
    results['original'] = session['original_array']
    results['current'] = session['current_array']
    
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True,port=8090)