'''
Helping

As my girlfriend's cat likes to say while knocking over my drink: "I'm HELPING!"

This library is dedicated to providing helpful information about Python objects.

The goal is "Readable information for real people."

TODO: Update classes() and exceptions() to act like functions() when no object is provided.
TODO: This implies changing symbols() to also accept a stack frame dictionary, or to automatically use those when builtins/no item is passed.
TODO: classes() should consider a module to be a class (if that doesn't happen automatically)
'''
from collections import OrderedDict
import inspect
import builtins

def symbols(item = builtins):
    ''' Returns a dictionary of information about the specified item. '''
    try:
        name = f'{item.__name__} ({item.__class__})'
    except:
        name = item.__class__

    info = OrderedDict()
    info['name'] = name
    for category_name in ['methods', 'classes', 'attributes', 'exceptions']:
        subcategories = OrderedDict()
        for sub in ['public', 'python', 'private']:
            subcategories[sub] = []
        info[category_name] = subcategories

    skip = {'None', 'False', 'True'}    # These don't get identified correctly, shouldn't be listed.

    for symbol in sorted(dir(item), key=str.lower):
        if symbol in skip: continue
        pointer = None
        try:
            pointer = getattr(item, symbol)
        except AttributeError:
            # We get here with Series.index, which blows up for some reason.
            # For now, assume in this case that it's a class.
            category = info['classes']

        if pointer is not None:
            #if isinstance(pointer, type):
            if inspect.isclass(pointer):
                # Some types like __builtins__.basestring can't be instantiated.
                thing = None
                try: thing = pointer()
                except: pass

                # Explicit check for 'is not None' because pandas classes raise an exception with an if check.
                if thing is not None and isinstance(thing, Exception):
                    category = info['exceptions']
                else:
                    category = info['classes']
            elif callable(pointer):
                category = info['methods']
            else:
                category = info['attributes']

        if symbol.startswith('__'):
            category['python'].append(symbol)
        elif symbol[0] == '_':
            category['private'].append(symbol)
        else:
            category['public'].append(symbol)
    return info

def functions(private = False, compact=False):
    ''' Prints out all functions available locally and globally, and Python built-in functions. '''
    
    # Need to get the stack frame of the caller so we can report on their environment. 
    caller_frame = inspect.stack()[1].frame

    all = {}
    for symbol_dict in (caller_frame.f_globals, caller_frame.f_locals):
        for key, value in symbol_dict.items():
            all[key] = value

    names = []
    for name in sorted(all, key=str.lower):
        item = all[name]
        if inspect.isfunction(item):
            if not private and name[0] == '_': continue
            names.append(f'{name}()')
    if names:
        print('Script functions:')
        if compact:
            print('   ' + ' '.join(names) + '\n')
        else:
            print('   ' + '\n   '.join(names) + '\n')

    print('Python built-in functions:')
    names = [f'{name}()' for name in symbols()['methods']['public']]
    if compact:
        print('   ' + ' '.join(names))
    else:
        print('   ' + '\n   '.join(names))


def _print_subcategory(info, category, sub, compact=False):
    if category == 'methods':
        template = '{}()'
    else:
        template = '{}'

    if not compact: template += '\n   '

    if sub == 'public':
        label = category
    else:
        label = f'{sub} {category}'

    items = [template.format(symbol) for symbol in info[category][sub]]
    text = ' '.join(items)
    print(f"  {label}:\n    {text}")

def _print_category(info, category, private = False, compact=False):
    ''' Returns a list of the methods for this item. '''
    if private:
        for sub in info[category]:
            if info[category][sub]:
                _print_subcategory(info, category, sub, compact=compact)
    else:
        if info[category]['public']:
            _print_subcategory(info, category, 'public', compact=compact)

def info(item = builtins, private = False, compact = False):
    '''
    A more readable and useful version of dir(), this presents useful information about an object or class.
    If no object or class is provided, defaults to showing info about builtins.

    By default doesn't show private (underscored) items. Pass 'private = True' to see private items.
    '''
    info = symbols(item)
    for category in info:
        if category == 'name':
            print(info['name'])
        else:
            _print_category(info, category, private=private, compact=compact)

def methods(item, private=False, compact=False):
    ''' Returns a list of the methods for this item. '''
    info = symbols(item)
    print(info['name'])
    _print_category(info, 'methods', private, compact)

def classes(item = builtins, private=False, compact=False):
    ''' Returns a list of the attributes for this item. '''
    info = symbols(item)
    print(info['name'])
    _print_category(info, 'classes', private, compact)

def attributes(item = builtins, private=False, compact=False):
    ''' Returns a list of the attributes for this item. '''
    info = symbols(item)
    print(info['name'])
    _print_category(info, 'attributes', private, compact)

def exceptions(item = builtins, private=False, compact=False):
    ''' Returns a list of the attributes for this item. '''
    info = symbols(item)
    print(info['name'])
    _print_category(info, 'exceptions', private, compact)

def test():
    #for key, value in symbols().items():
    #    print(f'{key}: {value}')
    #methods(inspect)
    #classes()
    #functions()
    #info()
    #docs()
    #help(False)
    #caller_stack = inspect.stack()[1]
    #frame = caller_stack.frame
    #print(info(frame))
    #print(f'Locals: {frame.f_locals}')
    #print(f'Globals: {frame.f_globals}')
#    print(inspect.stack())
    functions()

if __name__ == '__main__':
    # When this is run as a script, this serves as a test of the output.
    #info()
    test()
