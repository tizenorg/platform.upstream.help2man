#
# spec file for package help2man
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           help2man
Version:        1.40.10
Release:        0
License:        GPL-3.0+
Summary:        Create Simple Man Pages from --help Output
Url:            http://www.gnu.org/software/help2man/
Group:          Development/Tools/Doc Generators
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  gettext-tools
BuildRequires:  perl-gettext
Requires:       perl-gettext
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
help2man is a script to create simple man pages from the --help and
--version output of programs.

Since most GNU documentation is now in info format, this provides a way
to generate a placeholder man page pointing to that resource while
still providing some useful information.

%prep
%setup -q

%build
%configure --enable-nls
make %{?_smp_mflags}

%install
%make_install

%find_lang %{name} --with-man


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc COPYING NEWS README THANKS debian/changelog
%{_bindir}/help2man
%{_libdir}/help2man/
%doc %{_infodir}/help2man.info%{ext_info}
%doc %{_mandir}/man1/help2man.1%{ext_man}
%dir %{_mandir}/??
%dir %{_mandir}/??/man1

%changelog
